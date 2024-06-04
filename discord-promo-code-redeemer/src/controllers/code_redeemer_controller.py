import discord
import datetime
import logging

from discord.ext import commands

from ..models.code import Code
from ..models.redemption_log import RedemptionLog
from ..utils.validation_utils import validate_promo_code
from ..utils.scheduling_utils import schedule_code_redemption

class CodeRedeemerController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='redeem_code')
    async def redeem_code(self, ctx, promo_code: str):
        if validate_promo_code(promo_code):
            # Logic to redeem the promo code on Discord server
            redemption_log = RedemptionLog(code=promo_code, redeemed_at=datetime.datetime.now(), success=True)
            await ctx.send(f"Promo code {promo_code} redeemed successfully!")
            logging.info(f"Promo code {promo_code} redeemed successfully.")
        else:
            # Handle invalid promo code
            redemption_log = RedemptionLog(code=promo_code, redeemed_at=datetime.datetime.now(), success=False)
            await ctx.send(f"Error redeeming promo code {promo_code}. Please check the code and try again.")
            logging.error(f"Error redeeming promo code {promo_code}. Invalid code.")

def setup(bot):
    bot.add_cog(CodeRedeemerController(bot))