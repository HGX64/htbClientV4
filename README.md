# htbClientV4

***Language***
- [🇪🇸 Español](./README.es.md)
- 🇺🇸 English

**htbclientV4** is a tool that functions as a terminal-based client inspired by [s4vitar](https://github.com/s4vitar), but using some elements from version 4 of the Hackthebox API.

## How do I authenticate?
======
The first thing we need to do is go to the new interface of [Hack The Box](https://www.hackthebox.com). Once logged in, we should navigate to our profile settings. We will create a new "JSON Web Token" (JWTs have an "expiration date," so we should choose 1 year of validity). Anyway, I've created a small Python script you can use if you want to renew it frequently, but I recommend doing it through the web and adding 1 year of validity. Remember to verify the validity of the JWT if you find that the tool is not working.

<p align="center">
<img src="Images/get_jwt.png"
        alt="First"
        style="float: left; margin-right: 10px;" />
</p>

Now we need to obtain our "API TOKEN" from the old interface of [Hack The Box](https://hackthebox.eu/login). Once logged in, we will click on our profile and then on the "Settings" section.

<p align="center">
<img src="Images/localizar_settings.png"
        alt="Second"
        style="float: left; margin-right: 10px;" />
</p>

Once inside, we go to the API key section and copy it.

<p align="center">
<img src="Images/get_api_key.png"
        alt="Third"
        style="float: left; margin-right: 10px;" />
</p>

Now that we have the "JSON Web Token" and the "API Token," we need to input them into the code. Simply open the file, and they will be indicated in the first few lines.

<p align="center">
<img src="Images/authentication_into_the_code.png"
        alt="Fourth"
        style="float: left; margin-right: 10px;" />
</p>

This utility has an enumeration mode (**-e parameter**) that is quite fast.

<p align="center">
<img src="Images/enumeration_mode_panel.png"
        alt="Fifth"
        style="float: left; margin-right: 10px;" />
</p>

With it, we can list the machines deployed in the Hack The Box lab.

<p align="center">
<img src="Images/spawned_machines_file.png"
        alt="6"
        style="float: left; margin-right: 10px;" />
</p>

If we want to see the active machines, we also have that option, and those shown in the help panel.
<p align="center">
<img src="Images/active_machines_file.png"
        alt="7"
        style="float: left; margin-right: 10px;" />
</p>

We also have more customized search modes. With the "-s" parameter, we can search for anything, like names, IPs, dates, etc. If we want to search for machines based on the identifier, I recommend using the "-i" parameter as it is more precise.
<p align="center">
<img src="Images/search_machines_file.png"
        alt="8"
        style="float: left; margin-right: 10px;" />
</p>

If we inspect the help panel a bit more, we will notice that we can stop/reset/deploy/send flags (some are VIP).

<p align="center">
<img src="Images/help_panel_spawned_machines.png"
        alt="9"
        style="float: left; margin-right: 10px;" />
</p>

<p align="center">
<img src="Images/control_machines_file.png"
        alt="9"
        style="float: left; margin-right: 10px;" />
</p>

To send the flag, we will use the following method:

* htbclientV4 -f Lame=9d59efd64df62d3bc326dcb4ffc597cf,10

* The number 10 represents the personal difficulty we assign to the machine once completed.

* This tool is not as comprehensive as the one from s4vitar, but in some aspects, it is faster due to the combination of both versions of the Hack The Box API.

## Social media of s4vitar and link to their academy

[Youtube](https://www.youtube.com/s4vitar)  

[Instagram](https://www.instagram.com/s4vitarx/)  

[Twitter](https://twitter.com/S4vitar)  

[Linkedin](https://es.linkedin.com/in/s4vitar)  

[Academy](https://hack4u.io/)
