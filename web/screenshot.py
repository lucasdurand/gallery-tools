# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Grab a screenshot
#
# Let's get a look at a website!

# %%
from selenium import webdriver


# %%
def grab_screenshot(
    url,
    out_image="screenshot.png",
    driver_flags=["ignore-certificate-errors", "test-type", "headless"],
    jupyter=False,
):
    options = webdriver.ChromeOptions()
    for flag in driver_flags:
        options.add_argument(f"--{flag}")

    with webdriver.Chrome(options=options) as driver:
        driver.get(url)
        driver.save_screenshot(out_image)
    if jupyter:
        from IPython.display import Image

        return Image(out_image)


# %%
grab_screenshot("http://lucasdurand.xyz", "../my_website.png", jupyter=True)
