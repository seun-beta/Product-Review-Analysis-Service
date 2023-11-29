import pandas as pd
from vertexai.language_models import TextGenerationModel


generation_model = TextGenerationModel.from_pretrained("text-bison")


def zero_shot_prompt(product_review):

    prompt = f"""
        Classify this product review delimited by angle brackets into positive, negative or neutral. 
        Product review: <{product_review}>
        Sentiment: 
        """

    response = generation_model.predict(prompt=prompt).text

    return response


def single_shot_prompt(product_review):

    prompt = f"""
        Classify this product review delimited by angle brackets into positive, negative or neutral. 
        Product review: "I'm really disappointed about my phone and service. The phone went out on me over a week ago. I thought I was getting a deal but it seems like I'm the one who lucked out."
        Sentiment: Negative
        Product review: <{product_review}>
        Sentiment: 
        """

    response = generation_model.predict(prompt=prompt).text

    return response


def few_shot_prompt(product_review):

    prompt = f"""
        Classify this product review delimited by angle brackets into positive, negative or neutral. 
        Product review: "I'm really disappointed about my phone and service. The phone went out on me over a week ago. I thought I was getting a deal but it seems like I'm the one who lucked out."
        Sentiment: Negative
        Product review: My fiance had this phone previously, but caused many problems. So, of course, we decided to browse amazon for a replacement til' our contract is up! & so far so good!
        Sentiment: Positive
        Product review: I originally was using the Samsung S2 Galaxy for Sprint and wanted to return back to the Samsung EPIC 4G for Sprint because I really missed the keyboard. The camera works great, the video is great as well, and even the web browsing is decent and gives me what I need. I also notice that battery life lasts a little bit longer and charging the phone is much quicker than my Galaxy S2.
        Sentiment: Positive
        Product review: <{product_review}>
        Sentiment: 
        """

    response = generation_model.predict(prompt=prompt).text

    return response


df = pd.read_parquet("mobile_phone_reviews.parquet")

for index, row in df.iterrows():

    review = row["Reviews"]

    print(zero_shot_prompt(review))
    print(single_shot_prompt(review))
    print(few_shot_prompt(review))

    print(f"Row {index + 1}: Column 1 - {review}")