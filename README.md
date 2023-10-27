# ddns - dynamic DNS using Cloudflare's API

A python script that auto updates your DNS records to match your current public IP address

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Getting Started

First copy the example configuration file into the real one.

```sh
cp config-example.json config.json
```

Edit the `config.json` values to match the values of your cloudflare account

- The `email` is the email id that you use for cloudflare
- The `apikey` is your cloudflare account's API Key, It is your "Global API Key" and can be found [here](https://dash.cloudflare.com/profile/api-tokens) 
- The `zoneid` is the identifier of your zone, It can be found in the "API" section of your domain
- The `domain` is the subdomain/domain you want to use for this service. It should match the domain name of the zone you selected


## Deploy with Cron
To schedule automatic updates, consider using the cron job scheduler. Here's an example of how to set up a cron job to run the script every hour:

```sh
0 * * * * python3 ~/ddns/index.py
```

This will run the script every hour, updating the Cloudflare DNS records with the current public IP address.

## Development setup

Clone this repo and install packages listed in requirements.txt

```sh
git clone https://github.com/Aayush-Rajagopalan/ddns
cd ddns
pip install -r requirements.txt
```


## Contributing

1. Fork it (<https://github.com/Aayush-Rajagopalan/ddns/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
