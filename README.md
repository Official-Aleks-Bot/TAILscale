Disclaimer: This guide is for educational purposes only!

This is basicly a free VPN that uses github actions and tailscale form a Tailscale exit node as a vpn.

1. Can I change the loaction? - No

2. Can I do illegal things on it? - NO!

3. Is it free forever? - Yes

4. Any Limitaions? - Besides having to change servers every 6 hours, no.
   
5. Is it 24/7? - Yes

I works by using a VPS that github offers for free to build and compile code. Instead of compiling code, we are simple running a free tool called Tailscale.
Tailscale is a basicly used as a VPN server without port fowarding. This is required as github does not allow port forwarding.

=================
  How to set up
=================

Alright, in order to set it up, we need to do a few things first.

The first step is to make a Tailscale account.

Next, you want to go to settings and keys and create API access tokens. Create one with the longest expiration date possible because when it runs out, you'll need to create a new one. Write the API key down as we'll need it later. Write a note with the name TSKEY next to it.

After that, create an Auth key on Tailscale, and make sure to write this down as well. Make a note of the name APIKEY next to it.

Now, go to Tailscale DNS and look for the Tailnet name. Click the copy button. It should look like taildXXXXX.ts.net. Write a note of that with the key TAILNET next to it.

Now for the most challenging part. This step is easiest with a tool called Burp Suite, so I recommend you download it because that's how I'm going to explain this step. But if you know what you're doing, you can ignore this.
In Burp Suite, go to your GitHub account. Once you've forked this repository, go to the fork and click Actions. In Actions, click Tailscale Exit Node, then click Run workflow (the grey button). Now, before clicking the green run workflow button, turn on Intercept. Click the button, and you should see the request pop up on the left side of Burp Suite. Right-click inside that box, then click "Copy as CURL". Write down all of that with the note and the key CURL next to it.

Finally, go to GitHub, click Settings, then Secrets and variables. Next, click Actions, then create a New repository secret for each key with the corresponding variable.
Should look like this 

APIKEY - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
CURL - curl bunch of stuff here
TAILNET - taildXXXXX.ts.net
TSKEY - XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

=================
  How to set up
=================

Once youve done all that download tailscale on whatever you want to use the vpn on and sign in to. Connect to the exit node you want and youll connect! You can do up to 5 without trouble but I reccomend only 4. (And yes you can torrent LEGAL stuff on it)

