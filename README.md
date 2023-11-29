
# Sentiment Analysis for Product Reviews

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This project aims to perform sentiment analysis on product reviews using a language model. It provides functionalities for zero-shot, single-shot, and few-shot sentiment classification based on input review texts.

## Getting Started <a name = "getting_started"></a>

These instructions will help you set up the project on your local machine for development and testing purposes. See [deployment](#deployment) for information on deploying the project on a live system.

### Prerequisites

Ensure you have the following prerequisites installed:

- Python 3.x
- Google Cloud AI Platform package


### Installing

Follow these steps to set up the development environment:

1. Clone the repository: `git clone https://github.com/seun-beta/Product-Review-Analysis-Service.git`
2. Install required packages: `pip install -r requirements.txt`
3. Set up Google Cloud Platform (GCP) service account credentials:
   - Create a service account in GCP.
   - Generate a key and download the JSON file.
   - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the JSON file using `export GOOGLE_APPLICATION_CREDENTIALS="path-to-JSON-file"
`.

## Usage <a name = "usage"></a>

To utilize the sentiment analysis functionality, follow these steps:

1. Import the required libraries.
2. Call the `zero_shot_prompt`, `single_shot_prompt`, or `few_shot_prompt` functions with the product review text.
3. Interpret the generated sentiment classification.
