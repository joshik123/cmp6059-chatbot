# Train Delay Chatbot

This project is a simple train delay chatbot for Task 2.

The chatbot helps a passenger who is travelling from Weymouth to London Waterloo. If the train is delayed during the journey, the chatbot asks for some journey details and predicts the delay at the destination.

## What it does

- asks the passenger about their journey
- uses a trained machine learning model
- predicts the final delay
- gives an estimated arrival time
- checks station names
- explains if the delay is minor, moderate, or significant

## How to run

Install the required packages:

pip install -r requirements.tx

## Train the model

python train_model.py

## Run the chatbot:

python main.py

## Run evaluation

python src/evaluation.py



