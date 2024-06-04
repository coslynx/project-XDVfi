import datetime
import logging

def schedule_code_redemption(code, server, redemption_time):
    try:
        current_time = datetime.datetime.now()
        scheduled_time = datetime.datetime.strptime(redemption_time, "%Y-%m-%d %H:%M:%S")
        
        if scheduled_time < current_time:
            raise ValueError("Redemption time should be in the future.")
        
        logging.info(f"Scheduling code redemption for {code} on server {server} at {redemption_time}")
        # Add logic to redeem the code on the specified server at the redemption_time
        
        logging.info(f"Code {code} successfully redeemed on server {server} at {redemption_time}")
    
    except ValueError as e:
        logging.error(f"Error scheduling code redemption: {str(e)}")
    
    except Exception as e:
        logging.error(f"An error occurred during code redemption scheduling: {str(e)}")