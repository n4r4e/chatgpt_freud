# Talk to Freud - ChatGPT applied

This is a fictional conversation app with Freud created using OpenAI's ChatGPT.

Referenced the OpenAI's [Build your application tutorial](https://platform.openai.com/docs/quickstart/build-your-application). It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. 

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/).

2. Clone this repository.

3. Navigate into the project directory:

   ```bash
   $ cd chatgpt_freud
   ```

4. Create a new virtual environment:

   ```bash
   $ python -m venv venv
   $ . venv/bin/activate (or) . venv/Scripts/activate
   ```

5. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

6. Make a copy of the example environment variables file:

   ```bash
   $ cp .env.example .env
   ```

7. Add your [API key](https://beta.openai.com/account/api-keys) to the newly created `.env` file.

8. Run the app:

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000) or [http://127.0.0.1:5000](http://127.0.0.1:5000).
