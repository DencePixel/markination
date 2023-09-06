# Markination

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Markination is a versatile Python package that provides an easy-to-use Discord message paginator using the discord.py library.

## Features

- Discord Button Paginator
- Discord Dropdown Paginator
- Built-in support for navigation buttons (Next, Previous, First, Last).
- Designed for ease of use in your Discord bot projects.
- Extensible and open-source.

## Installation

[![License](https://media.discordapp.net/attachments/1093865249645547570/1147899684996780112/LibraryRequiresDiscordpy.png)](https://github.com/rapptz/discord.py)


You can install Markination using [Poetry](https://python-poetry.org/) and [PyPi](https://pypi.org/project/markination/)

```shell
poetry add markination
```

```python
pip install markination
```

## Usage

Simple Button Setup:
```python
from markination import ButtonPaginator
from discord.ext import commands
import discord

@bot.command()
async def paginator(ctx: commands.Context):
    # A list of embeds to paginate
    embeds = [discord.Embed(title="First embed"),         
            discord.Embed(title="Second embed"),
            discord.Embed(title="Third embed")]

    # Start the paginator
    await ButtonPaginator.Simple().start(ctx, pages=embeds)
```

Custom Buttons:
```python
from markination import ButtonPaginator
from discord.ext import commands
import discord
from discord import ui

@bot.command()
async def paginator(ctx: commands.Context):
    embeds = [discord.Embed(title="First embed"),         
            discord.Embed(title="Second embed"),
            discord.Embed(title="Third embed")]
    PreviousButton = discord.ui.Button(label=f"Previous")
    NextButton = discord.ui.Button(label=f"Next")
    FirstPageButton = discord.ui.Button(label=f"First Page")
    LastPageButton = discord.ui.Button(label=f"Last page")
    PageCounterStyle = discord.ButtonStyle.danger # Only accepts ButtonStyle instead of Button
    InitialPage = 0 # Page to start the paginator on.
    timeout = 0 # Seconds to timeout. Default is 60
    ephemeral = bool # Defaults to false if not passed in.
    await ButtonPaginator.Simple(
        PreviousButton=PreviousButton,
        NextButton=NextButton,
        FirstEmbedButton=FirstPageButton,
        LastEmbedButton=LastPageButton,
        PageCounterStyle=PageCounterStyle,
        InitialPage=InitialPage,
        timeout=timeout, ephemeral=ephemeral).start(ctx, pages=embeds)
```
Simple Dropdown Setup
```python
from markination import DropdownPaginator
from discord.ext import commands
import discord
from discord import ui

@bot.command()
async def dropdown(ctx):
    pages = [
        discord.Embed(title="Page 1", description="This is the first page."),
        discord.Embed(title="Page 2", description="This is the second page."),
        discord.Embed(title="Page 3", description="This is the third page.")
    ]

    await DropdownPaginator.Simple(ctx, pages, timeout=60, custom_error_embed=None).start(ctx)

```

Simple Dropdown With Custom Error Embed
```python
from markination import DropdownPaginator
from discord.ext import commands
import discord
from discord import ui

@bot.command()
async def dropdown(ctx):
    pages = [
        discord.Embed(title="Page 1", description="This is the first page."),
        discord.Embed(title="Page 2", description="This is the second page."),
        discord.Embed(title="Page 3", description="This is the third page.")
    ]
    custom_error_Embed = discord.Embed(title=f"My custom embed that sends when a random person uses my view!")
    await DropdownPaginator.Simple(ctx, pages, timeout=60, custom_error_embed=custom_error_Embed).start(ctx)
```
Pull Requests are always open!
