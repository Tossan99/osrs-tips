# Testing

This is the Testing section of the [README.md](README.md) file. It contains all the testing information for the project OSRS Tips.

Return to [README.md](README.md)
## Table of Contents

[Table of Contents](#table-of-contents)
- [Testing](#testing)
  - [Table of Contents](#table-of-contents)
- [Manual Testing](#manual-testing)
  - [Common Elements Testing](#common-elements-testing)
  - [Functionalities testing](#functionalities-testing)
- [Automated Testing](#automated-testing)
  - [Code Validation](#code-validation)
    - [HTML Validation](#html-validation)
    - [CSS Validation](#css-validation)
    - [Python Validation](#python-validation)
  - [Lighthouse Validation](#lighthouse-validation)
  - [Browser Validation](#browser-validation)
  - [User Testing](#user-testing)

[Back to top ⇧](#table-of-contents)

# Manual Testing
## Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Navbar

![Navbar Test](/README_files/manual_testing/navbar.gif)

- Footer

![Footer Test](/README_files/manual_testing/footer.gif)

- Responsivenes

![Responsivenes Test](/README_files/manual_testing/responsive.gif)

## Functionalities testing

- Home Page and Post Details

![Home Page and Post Details Test](/README_files/manual_testing/home.gif)

- Categories

![Categories Test](/README_files/manual_testing/categories.gif)

- Login

![Login Test](/README_files/manual_testing/login.gif)

- Signup

![Signup Test](/README_files/manual_testing/signup.gif)

- Logout

![Logout Test](/README_files/manual_testing/logout.gif)

- Create Post

![Create Post Test](/README_files/manual_testing/create.gif)

- Edit Post

![Edit Post Test](/README_files/manual_testing/edit-post.gif)

- Delete Post

![Delete Post Test](/README_files/manual_testing/delete-post.gif)

- Like Post

![Like Post Test](/README_files/manual_testing/like.gif)

- Comment on Post

![Comment on Post Test](/README_files/manual_testing/comment.gif)

- Edit Comment

![Edit Comment Test](/README_files/manual_testing/edit-comment.gif)

- Delete Comment

![Delete Comment Test](/README_files/manual_testing/delete-comment.gif)

- About Page

![About Page Test](/README_files/manual_testing/about.gif)

- Error 404 Page

![Error 404 Page Test](/README_files/manual_testing/error404.gif)

[Back to top ⇧](#table-of-contents)

# Automated Testing
## Code Validation

### HTML Validation
The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the `HTML`.

These are the results of the validation:

- Homepage

![Homepage HTML Validation](/README_files/validation/html-home.JPG)

- Login Page

![Login Page HTML Validation](/README_files/validation/html-signin.JPG)

- Logout Page

![Logout Page HTML Validation](/README_files/validation/html-logout.JPG)

- About Page

![About Page HTML Validation](/README_files/validation/html-about.JPG)

Some `HTML` files didn't pass due to some applications interfering with the `HTML`, but it passed when input manually.

[Back to top ⇧](#table-of-contents)

### CSS Validation
The [CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used for `CSS` code.

These are the results of the validation:

- CSS File

![CSS File](/README_files/validation/css.JPG)

[Back to top ⇧](#table-of-contents)

### Python Validation
For Python code, the [CI PEP8 online validator](https://pep8ci.herokuapp.com/) was used to validate the code.

Because there are so many, i have only included the results of the validation of the `views.py` file. All other Python files were validated and passed the test with same results. The only warnings are concerning comments and lines being too long.

- views.py File
![views.py Validation](/README_files/validation/python.JPG)

[Back to top ⇧](#table-of-contents)

## Lighthouse Validation
The [Lighthouse](https://developers.google.com/web/tools/lighthouse) tool was used to measure the performance of the website.

These are the results of the validation:

- Home Page

![Homepage Lighthouse Validation](/README_files/validation/lighthouse-home.JPG)

- About Page

![About Page Lighthouse Validation](/README_files/validation/lighthouse-about.JPG)

- Login Page

![Login Page Lighthouse Validation](/README_files/validation/lighthouse-login.JPG)

- Logout Page

![Logout Page Lighthouse Validation](/README_files/validation/lighthouse-logout.JPG)

- Signup Page

![Signup Page Lighthouse Validation](/README_files/validation/lighthouse-signup.JPG)

- Create Post Page

![Create Page Lighthouse Validation](/README_files/validation/lighthouse-create.JPG)

- Post Detail Page

![Post Detail Page Lighthouse Validation](/README_files/validation/lighthouse-postdetail.JPG)

- 404 Page

![404 Page Lighthouse Validation](/README_files/validation/lighthouse-404.JPG)

[Back to top ⇧](#table-of-contents)

## Browser Validation
The website was tested with **pass** on the following browsers:
Google Chrome, Microsoft Edge, Mozilla Firefox, Opera, Safari.

## User Testing
The website was tested by differen users, with different devices and browsers.
There were several suggestions for improvement, which were implemented in the future. The bugs discovered were fixed.

[Back to top ⇧](#table-of-contents)