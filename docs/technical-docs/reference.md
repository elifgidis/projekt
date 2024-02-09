---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label }
[Elif Gidis]

# [Reference documentation]
{: .no_toc }



<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>


# Home Page Access index()

Route: /

Methods: GET

Purpose: 
Serves the home page of the application. This function renders the base template, providing users with an entry point to the application, including navigation to login, register, or select topic.



# User Registration  register()

Route: /register/

Methods: GET, POST

Purpose: 
This function handles user registration. It displays a registration form and processes the form data to create a new user account.

# User Login login()

Route: /login/

Methods: GET, POST

Purpose: 
Manages the user login process. It retrieves and verifies the user's credentials against the database. If authentication is successful, it redirects the user to the select topic page; otherwise, it redirect back to the login page.

# Logout logout()

Route: /logout/

Methods: GET

Purpose:
Handles user logout. This function helps users to securely exit their account.


# Select Quiz Topic select_topic()

Route: /select_topic/

Methods: GET, POST

Purpose: 
Handles the user's topic selection. It stores the selected topic in the session for use in displaying relevant quiz questions.


# Show Quiz Questions show_questions()

Route: /show_questions/

Methods: GET

Purpose: 
Displays quiz questions based on selected topic. It retrieves questions from a pre-defined dataset and renders them on the questions page.


# Submit Quiz submit_quiz()

Route: /submit_quiz/

Methods: POST

Purpose:
Processes the answers submitted by the user for a quiz, calculates the score based on correct answers, and displays the results along with correct answers for review.


# Database Check check_db()

Route: /check_db/

Methods: GET

Purpose: 
A utility route to verify database connectivity and functionality by listing all users in the database..




# Display Specific Score   score_page(score)

Route: /score/<int:score>

Methods: GET

Purpose:
This route dynamically displays a specific score passed in the URL to the user. 


# Show Cumulative Score show_score()

Route: /score

Methods: GET

Purpose:
Designed for users to view their quiz score and total questions  after submitting a quiz. 




![image](https://github.com/elifgidis/projekt/assets/154848427/3debfb75-e5fb-48ee-9b56-78859a80f086)
![image](https://github.com/elifgidis/projekt/assets/154848427/44533ff9-0d7e-4a19-abcd-0694f5f29d7d)
![image](https://github.com/elifgidis/projekt/assets/154848427/efabb914-1eeb-4397-b455-cea445a72070)
![image](https://github.com/elifgidis/projekt/assets/154848427/534454ea-7124-40d4-9c0e-b34fdeb09330)
![image](https://github.com/elifgidis/projekt/assets/154848427/523b935e-8bf3-42b2-a4da-739a3b84f7fb)
![image](https://github.com/elifgidis/projekt/assets/154848427/38c16c21-581e-4e2c-b595-ed58d7924a65)
![image](https://github.com/elifgidis/projekt/assets/154848427/a7b3565b-bf17-439a-b0e7-b48a6d563b6a)













