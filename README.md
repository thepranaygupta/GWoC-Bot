<div align="center">
<h1>GirlScript Winter of Contributing Twitter Bot</h1>
</div>

[![GitHub issues](https://img.shields.io/github/issues/thepranaygupta/GWoC-Bot)](https://github.com/thepranaygupta/GWoC-Bot/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/thepranaygupta/GWoC-Bot/pulls)
[![GitHub forks](https://img.shields.io/github/forks/thepranaygupta/GWoC-Bot)](https://github.com/thepranaygupta/GWoC-Bot/network)
[![GitHub stars](https://img.shields.io/github/stars/thepranaygupta/GWoC-Bot)](https://github.com/thepranaygupta/GWoC-Bot/stargazers)
[![Watchers](https://img.shields.io/github/watchers/thepranaygupta/GWoC-Bot)](https://github.com/thepranaygupta/GWoC-Bot/watchers)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Ftwitter.com%2FGWoC_Bot)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fthepranaygupta%2FGWoC-Bot)

### A Twitter Bot that retweets and likes tweets with the hashtag [`#girlscriptwoc`](https://twitter.com/search?q=%23girlscriptwoc) and [`#girlscript`](https://twitter.com/search?q=%23girlscript), and also follows the user.

<div align="center">
<a href="https://twitter.com/GWoC_Bot">
<img src="https://user-images.githubusercontent.com/64855541/134766679-c0a62e68-7663-4823-afb7-4ef21e9095d0.jpg" alt="GirlScript Winter of Contributing Bot on Twitter" width=500px>
</a>
</div>

## Installation 📥

- Clone the repo

  ```
  $ git clone https://github.com/thepranaygupta/GWoC-Bot.git
  ```

- Install [Tweepy](http://www.tweepy.org/)  - An easy-to-use Python library for accessing the **Twitter API**.

  ```
  $ pip install tweepy
  ```

## Working ⚙️

- Create a new Twitter account for your bot and Sign up for [Twitter Developer Account](https://developer.twitter.com/en/apply-for-access).
- Make sure you fully understand [Twitter's Rules on Automation](https://support.twitter.com/articles/76915). Play nice. Don't spam!
- Click on [Create an app](https://developer.twitter.com/en/apps). This is where you'll generate your keys, tokens, and secrets.
- Enter the details and keep safe the access tokens generated.
- Edit the [bot.py](./bot.py) file accordingly.

## Deployment on [Heroku](https://www.heroku.com/) ⚒️

Follow all the steps as shown in this [YouTube Tutorial](https://youtu.be/BPvg9bndP1U). <br>
You need to make three different files :

- [runtime.txt](./runtime.txt) (Includes Python Version `python-3.8.12`)
- [requirements.txt](./requirements.txt) (`pip freeze > requirements.txt`)
- [Procfile](./Procfile) (`worker: python bot.py`)

**Note**: Make sure that your [bot.py](./bot.py) file and the files generated above are in the same directory.

## License 🧾

The GirlScript Winter of Contributing Twitter Bot is released under the under terms of the [MIT License](./LICENSE).

## Contact 📬

If you are stuck anywhere you can contact me via [Twitter](https://twitter.com/thepranaygupta) or [LinkedIn](https://www.linkedin.com/in/thepranaygupta/) I will be glad to help you.😊 <br>
Check out my other repositories [here](https://github.com/thepranaygupta?tab=repositories).
