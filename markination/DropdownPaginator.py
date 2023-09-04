
from __future__ import annotations

import discord
from discord.ext import commands

class Simple(discord.ui.Select):
    """
    Dropdown Paginator.

    Parameters:
    ----------
    timeout: int
        How long the Paginator should timeout in, after the last interaction. (In seconds) (Overrides default of 60)
    custom_error_embed: Embed
        The embed that sends when someone uses somebody elses panel
    
    Pages: list
        The embeds to send.
    InitialPage: int
        Page to start the pagination on.

    """
    def __init__(self,ctx, pages: list[discord.Embed], timeout: int, custom_error_embed: discord.Embed, initial_page: int = 0):
        options = [
            discord.SelectOption(label=page.title, value=str(i)) for i, page in enumerate(pages)
        ]
        super().__init__(placeholder='Choose a page...', min_values=1, max_values=1, options=options)
        self.pages = pages
        self.current_page = initial_page
        self.ctx = ctx
        self.timeout = timeout
        self.custom_error_embed = custom_error_embed

    async def callback(self, interaction: discord.Interaction):
        selected_values = interaction.data.get('values')
        if interaction.user.id != self.ctx.author.id:
            if self.custom_error_embed:
                return await interaction.response.send_message(embed=self.custom_error_embed, ephemeral=True)
                
            embed = discord.Embed(description=f"**{interaction.user.global_name},** this is not your view!",
                                  color=discord.Colour.dark_embed())
            embed.set_footer(text=f"Markination - 2023")
            return await interaction.response.send_message(embed=embed, ephemeral=True)

        if not selected_values:
            return

        selected_page = int(selected_values[0])

        if selected_page < 0 or selected_page >= len(self.pages):
            return

        if selected_page == self.current_page:
            return

        self.current_page = selected_page
        selected_embed = self.pages[selected_page]

        try:
            await interaction.message.edit(embed=selected_embed, view=self.view)
        except discord.errors.NotFound:
            return

        await interaction.response.defer()

    def update_options(self):
        self.options = [
            discord.SelectOption(label=f"Page {i+1}", value=str(i)) for i in range(len(self.pages))
        ]
        
    async def start(self, ctx: discord.Interaction|commands.Context):
        if isinstance(ctx, discord.Interaction):
            ctx = await commands.Context.from_interaction(ctx)
    
        view = discord.ui.View(timeout=self.timeout)
        dropdown = Simple(ctx=ctx, pages=self.pages, timeout=self.timeout, custom_error_embed=self.custom_error_embed, initial_page=0)
        view.add_item(dropdown)
        self.message = await ctx.send(embed=self.pages[self.current_page], view=view, ephemeral=True)

    def update_options(self):
        self.options = [
            discord.SelectOption(label=f"Page {i+1}", value=str(i)) for i in range(len(self.pages))]