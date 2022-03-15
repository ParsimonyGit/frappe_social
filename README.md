## Frappe Social

App to contain social wall feature of frappe version 12 that works with frappe version-13.

### Introduction

Frappe Social is an app built on top of Frappe to work with version-13. It holds the social wall page which used to be in frappe version-12 but later got removed from frappe version-13.
Visit {domain_name}//app/Social/home. Also, to get the chat feature on the page working install [Frappe's chat app](https://github.com/frappe/chat) using: ```$ bench get-app chat```

### Screenshots
1. The Homepage:
![The Homepage](https://github.com/DeeMysterio/frappe_social/blob/master/screenshots/social_homepage.png)

2. Chat Feature:
![Chat](https://github.com/DeeMysterio/frappe_social/blob/master/screenshots/social_chat.png)

3. Make a Post:
![Make Post](https://github.com/DeeMysterio/frappe_social/blob/master/screenshots/social_post.gif)

### Installation

Once you have a basic site created with the app Frappe, just install Frappe Social on top of it using the below command:
```sh
$ bench get-app https://github.com/DeeMysterio/frappe_social.git
```

### License

GNU GPL V3. See [license.txt](https://github.com/DeeMysterio/frappe_social/blob/master/license.txt) for more information.
