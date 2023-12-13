import discord
from discord import app_commands

import random
id_do_servidor = 702216338000576632


class client(discord.Client):

  def __init__(self):
    super().__init__(intents=discord.Intents.default())
    self.synced = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:
      await tree.sync(
        guild=discord.Object(id=id_do_servidor)
      )
      self.synced = True
    print(f"Entramos como {self.user}.")


aclient = client()
tree = app_commands.CommandTree(aclient)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='teste',
              description='Testando')
async def slash2(interaction: discord.Interaction):
  await interaction.response.send_message(f"Estou funcionando!",
                                          ephemeral=True)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='canal',
              description='procurando...'
              )
async def slash3(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"https://www.youtube.com/@TheRealOnesTRO", ephemeral=False)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='sorte',
              description='qual sera?')
async def slash4(interaction: discord.Interaction):
  numero2 = random.randint(1, 100)
  await interaction.response.send_message(
    f"{numero2}% de sorte!!:four_leaf_clover:", ephemeral=False)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='facul',
              description='faculdade')
async def slash5(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"cursando 2° semestre de TSI no IFB ", ephemeral=False)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='tempo',
              description='daqui a pouco passa...')
async def slash6(interaction: discord.Interaction):
  numero2 = random.randint(1, 60)
  await interaction.response.send_message(
    f"daqui a {numero2} minutos passa um baú!!", ephemeral=False)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='faz',
              description='oque faz?')
async def slash7(interaction: discord.Interaction):
  await interaction.response.send_message(
    f"Vice-presidente do Centro acadêmico de TSI - Programador WEB e back-end.", ephemeral=False)


aclient.run(
  'MTA2OTkwNzk1NDQxMDcyMTI5MA.GsEn4u.OEm39yOc3I1VkFogypXFB-uRZD0Cu1ft4VdAHA')

