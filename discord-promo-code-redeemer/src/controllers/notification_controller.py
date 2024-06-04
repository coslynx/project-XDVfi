import discord
import logging
from discord.ext import commands

from ..models.redemption_log import RedemptionLog

class NotificationController:
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def notify_successful_redemption(self, user_id: int, code: str):
        user = self.bot.get_user(user_id)
        if user:
            await user.send(f"Congratulations! Your promo code {code} has been successfully redeemed.")
            RedemptionLog.log_success(user_id, code)
        else:
            logging.error(f"User with ID {user_id} not found for successful redemption notification.")

    async def notify_failed_redemption(self, user_id: int, code: str, error_message: str):
        user = self.bot.get_user(user_id)
        if user:
            await user.send(f"Failed to redeem promo code {code}. Error: {error_message}")
            RedemptionLog.log_failure(user_id, code, error_message)
        else:
            logging.error(f"User with ID {user_id} not found for failed redemption notification.")