### Introduction

Frappe Social is an app built on top of [Frappe](https://github.com/frappe/frappe) to work with version-13. It holds the "Social Wall" page which used to be in version-12 but later got removed from version-13.

To view the social wall, visit `/app/social/home`. To get the chat feature working, install [Frappe's chat app](https://github.com/frappe/chat) using:

```sh
$ bench get-app chat
```

### Screenshots
1. Homepage:
![The Homepage](https://github.com/ParsimonyGit/frappe_social/blob/master/screenshots/social_homepage.png)

2. Chat Feature:
![Chat](https://github.com/ParsimonyGit/frappe_social/blob/master/screenshots/social_chat.png)

3. Make a Post:
![Make Post](https://github.com/ParsimonyGit/frappe_social/blob/master/screenshots/social_post.gif)

### Installation

Once you have a basic site created with the app Frappe, just install Frappe Social on top of it using the below command:
```sh
$ bench get-app https://github.com/ParsimonyGit/frappe_social.git
```

### Authors

- Initial compatibility work started by [DeeMysterio](https://github.com/DeeMysterio/frappe_social).

### License

GNU GPL V3. See [license.txt](https://github.com/ParsimonyGit/frappe_social/blob/master/license.txt) for more information.
