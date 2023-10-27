import requests
import json

# Config that will be used for sending API calls to Cloudflare
config = json.load(open('config.json'))
base_url = "https://api.cloudflare.com/client/v4/zones"
headers = {
    "X-Auth-Email": config["email"],
    "X-Auth-Key": config["apikey"],
    "Content-Type": "application/json"
}

# This function Gets the Current Public IP Address
def getPublicIP():
    try:
        res = requests.get("https://ipinfo.io/json")
        json = res.json()
        return json['ip']
    except Exception as e:
        print("❌ Error in Getting Public IP Address.")
        return 0

# This function Checks if the domain provided is there in cloudflare.
# If it's there, then it would return the IP address/host of that DNS record
# If it's not there, then it would create a new DNS record with the domain name provided with the public IP address
def getCloudflareIP():
    try:
        records = requests.get(
            f"{base_url}/{config['zoneid']}/dns_records/", headers=headers).json()['result']
        # Checks through all the records to find one that matches the domain name provided
        for i in records:
            if i['name'] == config['domain']:
                return i['content']
            else:
                # Creates a new record if it doesn't exist
                res = requests.post(f"{base_url}/{config['zoneid']}/dns_records/", headers=headers, json={
                    'content': getPublicIP(),
                    'name': config['domain'],
                    'type': 'A',
                    'comment': 'created using ddns'
                })
                return 1             
    except:
        print("❌ Error in Getting Cloudflare DNS Records. Try Checking your API Key or Zone ID")
        return 0

# This function updates the DNS Record of the domain provided
# The record type gets converted to an "A" record 
def updateDNS(ip):
    try:
        res = requests.patch(f"{base_url}/{config['zoneid']}/dns_records/{config['domainid']}", headers=headers, json={
            "content": ip,
            "type": "A"
        })
        if res.ok != True:
            print("❌ Error in Updating Cloudflare DNS Records. Try Checking your API Key or Zone ID")
    except:
        return 0

# Primary Function
if __name__ == "__main__":
    publicip = getPublicIP()
    cloudflareip = getCloudflareIP()

    if cloudflareip == 1:
        print(f"✅ Created {config['domain']}")
    
    # Checks if both the getPublicIP and getCloudflareIP functions returned a proper response
    if publicip and cloudflareip:
        # If the IP Addresses do not match, update the DNS Record
        if publicip != cloudflareip:
            updateDNS(publicip)
            # Checks if the updateDNS function returned a proper response
            if updateDNS:
                print(f"✅ Updated {config['domain']}'s IP Address to", publicip)
            else:
                print("❌ Error in Updating Domain's IP Address")
        else:
            print("⌚ IP Addresses match")
