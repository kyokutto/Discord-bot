import os
import random

from dotenv import load_dotenv
import discord
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


intent = discord.Intents.default()
bot = commands.Bot(command_prefix="1", intents=intent)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user.name} has connected to Discord server!")

@bot.tree.command(name="hello", description="Says hello to the user who invoked the command.")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello, {interaction.user.display_name}!")

@bot.tree.command(name="coinflip", description="Flips a coin and returns the result.")
async def coinflip(interaction: discord.Interaction):
    result = random.choice(["Heads", "Tails"])
    await interaction.response.send_message(f"{interaction.user.display_name} flipped the coin and it landed on: {result}!")

@bot.tree.command(name="add", description="Adds two numbers and returns the result.")
async def add(interaction: discord.Interaction, num1: int, num2: int):
    result = num1 + num2
    await interaction.response.send_message(f"{interaction.user.display_name} added {num1} and {num2} and the result is: {result}!")

@bot.tree.command(name="8ball", description="Ask the -magic- 8ball a question and get and answer.")
async def eight_ball(interaction: discord.Interaction, question: str):
    responses = [
        "Yes, definitely!",
        "More likely yes than not.",
        "Maybe.",
        "I don't think so.",
        "It's possible, but not likely.",
        "More likely no than yes.",
        "No, definitely not.",
        "Never gonna happen."
    ]
    answer = random.choice(responses)
    await interaction.response.send_message(f"{interaction.user.display_name} asked: '{question}'\nThe 8ball says: '{answer}'")

if TOKEN is None:
    raise SystemExit("Couldn't find DISCORD_TOKEN in .env file. Make sure to set it before running the bot.")

bot.run(TOKEN)