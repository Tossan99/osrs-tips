# Testing

This is the Testing section of the [README.md](README.md) file. It contains all the testing information for the project OSRS Tips.

Return to [README.md](README.md)
## Table of Contents

[Testing](#testing)
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

## Manual Testing
### Common Elements Testing
Manual testing was conducted on the following elements that appear on every page:

- Navbar

![Navbar Test](./docs/images/manual_testing/navbar.gif)

- Footer

![Footer Test](./docs/images/manual_testing/footer.gif)

### Functionalities testing

- Categories

![Categories Test](./docs/images/manual_testing/contact.gif)

- Login

![Login Test](./docs/images/manual_testing/login.gif)

- Register

![Register Test](./docs/images/manual_testing/registration.gif)

- Logout

![Logout Test](./docs/images/manual_testing/logout.gif)

- Create Post

![Add Book Test](./docs/images/manual_testing/add_book.gif)

- Edit Post

![Edit Book Test](./docs/images/manual_testing/edit_book.gif)

- Delete Post

![Delete Book Test](./docs/images/manual_testing/delete_book.gif)

- Post Details

![Book Details Test](./docs/images/manual_testing/book_details.gif)

- Like Post

![Book Details Test](./docs/images/manual_testing/book_details.gif)

- Comment on Post

![Book Details Test](./docs/images/manual_testing/book_details.gif)

- Edit Comment

![Book Details Test](./docs/images/manual_testing/book_details.gif)

- Delete Comment

![Book Details Test](./docs/images/manual_testing/book_details.gif)

- About Page

![Contact Page Test](./docs/images/manual_testing/contact.gif)

- Error 404 Page

![Error 404 Page Test](./docs/images/manual_testing/contact.gif)

[Back to top ⇧](#table-of-contents)

## Automated Testing
### Code Validation

#### HTML Validation
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

- 404 Page (Manual Insertion)
![404 Page HTML Validation](./docs/images/html_css_validation/404_html.png)

[Back to top ⇧](#table-of-contents)

#### CSS Validation
The [CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used for `CSS` code.

These are the results of the validation:

- CSS File
![CSS File](/README_files/validation/css.JPG)

[Back to top ⇧](#table-of-contents)

#### Python Validation
For Python code, the [CI PEP8 online validator](https://pep8ci.herokuapp.com/) was used to validate the code.

Because there are so many, i have only included the results of the validation of the `views.py` file. All other Python files were validated and passed the test with same results. The only warnings are concerning comments and lines being too long.

- views.py File
![views.py Validation](/README_files/validation/python.JPG)

[Back to top ⇧](#table-of-contents)

### Lighthouse Validation
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

### Browser Validation
The website was tested with **pass** on the following browsers:
Google Chrome, Microsoft Edge, Mozilla Firefox, Opera, Safari.

### User Testing
The website was tested by differen users, with different devices and browsers.
There were several suggestions for improvement, which were implemented in the future. The bugs discovered were fixed.

[Back to top ⇧](#table-of-contents)