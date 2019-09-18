# Description
This basic script will generate multiple bootstrap packages for Palo Alto Networks firewalls. If you are deploying more than a single firewall and need to generate unique init-cfg.txt files, this simple python script will do just that.

There are four files in this example.
* generate-bootstrap.py - the python script for generating the bootstrap package
* vars.text - this file holds the variables that you would like to change in the init-cfg.txt
* init-cfg-template.txt - this is the base init-cfg that will be replicated for each firewall
* authcodes-template.txt - place the authcode into this text file.

After running the script, a bootstrap directory will be created for each variable listed in the vars.text file.  The main directory will contain the four required subdirectories
* config
* content
* license
* software

# Support

I'm providing this script as an example to generate multiple bootstrap files for Palo Alto Networks Firewalls.  There is no  support.  Feel free to modify the script to suite your needs.

# References
https://docs.paloaltonetworks.com/vm-series/9-0/vm-series-deployment/bootstrap-the-vm-series-firewall/bootstrap-package.html
