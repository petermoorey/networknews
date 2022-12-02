# networknews.app

A weekly email with curated high-quality news, articles and blog posts from the computer networking industry.

## Solution

### Core Components

- Scheduled function to orchestrate creation of a weekly email
- Triggered function to collect news, articles and blog posts
- Triggered function to analyse items and assign a rating and topics via machine learning
- Triggered function to create and send email to subscribers
- Queue/service bus for communication between functions
- Data store to retain collected item URLs, abstract, rating, and tagged topics
- Data store to define sources of news, articles, and blog posts
