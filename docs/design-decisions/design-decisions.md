---
title: Design Decisions
nav_order: 3
---


# [Design decisions]
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: [SQL vs SQlAlchemy ?]

### Meta
Status: Decided
Updated:01.12.2023

Problem Statement
Deciding between using raw SQL and SQLAlchemy for database interactions to optimize development efficiency and application performance.

Decision
I chose SQLAlchemy for its ORM capabilities, allowing for more intuitive interaction with the database and better long-term maintainability.

Given Options:
SQL
Pros: Direct control over queries, potential for optimized performance.
Cons: Higher complexity in query management, increased development time for complex operations.

SQLAlchemy
Pros: Simplifies database operations with ORM, enhances code readability and maintainability.
Cons: Possible overhead from ORM layer, slight learning curve for optimal usage.

## 02: [SQLite vs. MySQL ?]

### Meta

Status: Decided
Updated: 03.12.2024

Problem Statement
Choosing the most suitable database management system considering factors like project size, scalability, and complexity.

Decision
SQLite was selected for its simplicity and ease of integration with small to medium-sized projects, reducing the need for extensive server setup.

Regarded Options:
SQLite
Pros: Lightweight, no need for a separate server, ideal for development and smaller applications.
Cons: Not suitable for high-concurrency applications or large databases.

MySQL
Pros: Scalable, supports large databases and high concurrency, robust features for complex applications.
Cons: Requires more setup and resources, overkill for small projects.

## 03: [Jinja vs. Django ?]

Status: Decided
Updated: 30.11.2023

Problem Statement
Selecting a template engine that offers flexibility, efficiency, and ease of use for our web development needs.

Decision
Jinja was chosen for its speed and flexibility, allowing for quick development cycles and easy integration with Flask.

Provided Options:
Jinja
Pros: High performance, straightforward syntax, versatile for various projects.
Cons: Less integrated features compared to Django's templating.

Django
Pros: Comprehensive features, integrated with Django's ecosystem.
Cons: Less flexibility for projects not using Django, steeper learning curve.

## 04: [Secure Authentication]
Secure authentication mechanisms are employed to protect user accounts and personal information. E.g. CSRF tokens for jinja.

## 05: [Minimalistic Design]
I chose a simple and effective design for the app's user interface. By adopting a minimalistic approach, the interface is kept clean and free from distractions. This decision is grounded not just in aesthetic preference but for usability.

## 06: [ Data Minimization Principle]
In line with the principle of data minimization, the app collects only the necessary data required for its functionality, like email addresses for login.


## 07: [Modular Design for Scalability]
Lastly, the app was conceived with a modular design, prioritizing future scalability and ease of maintenance. Following Flask modular structure to keep bug fixes & maintenance easier.

