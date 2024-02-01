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

- Favicon

![Favicon Test](./docs/images/manual_testing/favicon.png)

### Functionalities testing
- Login

![Login Test](./docs/images/manual_testing/login.gif)

- Register

![Register Test](./docs/images/manual_testing/registration.gif)

- Logout

![Logout Test](./docs/images/manual_testing/logout.gif)

- Profile Update

![Profile Update Test](./docs/images/manual_testing/profile_update.gif)

- Profile Delete

![Profile Delete Test](./docs/images/manual_testing/profile_delete.gif)

- Verify Profile Deletion (and all book records associated with the user)

![Verify Profile Deletion Test](./docs/images/manual_testing/delete_verify.gif)

- Add Book

![Add Book Test](./docs/images/manual_testing/add_book.gif)

- Edit Book

![Edit Book Test](./docs/images/manual_testing/edit_book.gif)

- Delete Book

![Delete Book Test](./docs/images/manual_testing/delete_book.gif)

- Find Book

![Find Book Test](./docs/images/manual_testing/find_book.gif)

- Book Details

![Book Details Test](./docs/images/manual_testing/book_details.gif)

- Favourites Page

![Favourites Page Test](./docs/images/manual_testing/favourites.gif)

- Contact Page

![Contact Page Test](./docs/images/manual_testing/contact.gif)

## Automated Testing
### Code Validation

#### HTML Validation
The [W3C Markup Validator](https://validator.w3.org/) service was used to validate the `HTML`.

These are the results of the validation:

- Homepage
![Homepage HTML Validation](./docs/images/html_css_validation/homepage_html.png)

- Login Page
![Login Page HTML Validation](./docs/images/html_css_validation/login_html.png)

- Register Page
![Register Page HTML Validation](./docs/images/html_css_validation/register_html.png)

- Contact Page
![Contact Page HTML Validation](./docs/images/html_css_validation/contact_html.png)

- Find Book Page
![Find Book Page HTML Validation](./docs/images/html_css_validation/find_book_html.png)

- Add Book Page
![Add Book Page HTML Validation](./docs/images/html_css_validation/add_book_html.png)

- User Page (My Books Page)
![User Page (My Books Page) HTML Validation](./docs/images/html_css_validation/user_page_html.png)

- Book Details Page
![Book Details Page HTML Validation](./docs/images/html_css_validation/book_detail_html.png)

- Edit Book Page (Update Book)
![Edit Book Page HTML Validation](./docs/images/html_css_validation/edit_book_html.png)

- Delete Book Page
![Delete Book Page HTML Validation](./docs/images/html_css_validation/delete_book_html.png)

- User Favourites Page
![User Favourites Page HTML Validation](./docs/images/html_css_validation/favourites_html.png)

- User Profile Page
![User Profile Page HTML Validation](./docs/images/html_css_validation/user_profile_html.png)

- Update Profile Page
![Update Profile Page HTML Validation](./docs/images/html_css_validation/user_profile_update_html.png)

- 404 Page (Manual Insertion)
![404 Page HTML Validation](./docs/images/html_css_validation/404_html.png)

[Back to top ⇧](#table-of-contents)

#### CSS Validation
The [CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used for `CSS` code.

These are the results of the validation:

- Homepage CSS File
![Homepage CSS Validation](./docs/images/html_css_validation/homepage_css.png)

- General CSS File
![General CSS Validation](./docs/images/html_css_validation/style_css.png)

[Back to top ⇧](#table-of-contents)


The [JSHint JavaScript Code Quality Tool](https://jshint.com/) was used to validate the sites `JS` code.

- Contact JS File
![Contact JS Validation](./docs/images/js_validation/contact_js_validation.png)

- Find Book JS File
![Find Book JS Validation](./docs/images/js_validation/search_js_validation.png)

- Script JS File
![Script JS Validation](./docs/images/js_validation/script_js_validation.png)


#### Python Validation
For Python code, the [CI PEP8 online validator](https://pep8ci.herokuapp.com/) was used to validate the code.

Because there are so many, the developer includes here only the results of the validation of the `settings.py` file. All other Python files were validated and passed the test with same results.

- Settings.py File
![Settings.py Validation](./docs/images/python_validation/settings_py.png)

[Back to top ⇧](#table-of-contents)


### Lighthouse Validation
The [Lighthouse](https://developers.google.com/web/tools/lighthouse) tool was used to measure the performance of the website.

These are the results of the validation:

- Homepage

![Homepage Lighthouse Validation](./docs/images/lighthouse/home_lighthouse.png)

- Login Page

![Login Page Lighthouse Validation](./docs/images/lighthouse/login_lighthouse.png)

- Register Page

![Register Page Lighthouse Validation](./docs/images/lighthouse/register_lighthouse.png)

- Contact Page

![Contact Page Lighthouse Validation](./docs/images/lighthouse/contact_lighthouse.png)

- Find Book Page

![Find Book Page Lighthouse Validation](./docs/images/lighthouse/search_lighthouse.png)

- Add Book Page

![Add Book Page Lighthouse Validation](./docs/images/lighthouse/add_book_lighthouse.png)

- User Page (My Books Page)

![User Page (My Books Page) Lighthouse Validation](./docs/images/lighthouse/user_page_lighthouse.png)

- Book Details Page

![Book Details Page Lighthouse Validation](./docs/images/lighthouse/book_detail_lighthouse.png)

- Edit Book Page (Update Book)

![Edit Book Page Lighthouse Validation](./docs/images/lighthouse/edit_book_lighthouse.png)

- Delete Book Page

![Delete Book Page Lighthouse Validation](./docs/images/lighthouse/delete_book_lighthouse.png)

- User Favourites Page

![User Favourites Page Lighthouse Validation](./docs/images/lighthouse/favourites_lighthouse.png)

- User Profile Page

![User Profile Page Lighthouse Validation](./docs/images/lighthouse/user_profile_lighthouse.png)

- Update Profile Page

![Update Profile Page Lighthouse Validation](./docs/images/lighthouse/update_profile_lighthouse.png)

- 404 Page couldn't be tested with Lighthouse

[Back to top ⇧](#table-of-contents)

### Browser Validation
The website was tested with **pass** on the following browsers:
Google Chrome, Microsoft Edge, Mozilla Firefox, Opera, Safari, Vivaldi, Brave.

In regards to **responsiveness**, the website was tested with **pass** on the following devices:
The website was tested with **pass** on the following devices:
- Laptop ThinkPad x270 on Linux Manjaro 3.0 Uranos
- Ipad Air 2 on iOS 16.7
- Iphone 12 on iOS 16.7
- Xiaomi Mi Note 11 Pro on Android 14.0.1

### User Testing
The website was tested by differen users, with different devices and browsers. The feedback was positive and the website was easy to use and navigate.
There were several suggestions for improvement, which were implemented in the future. The bugs discovered were fixed.

[Back to top ⇧](#table-of-contents)