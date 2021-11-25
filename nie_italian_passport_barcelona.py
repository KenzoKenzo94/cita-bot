import os
import sys

from bcncita import CustomerProfile, DocType, Office, OperationType, Province, try_cita

if __name__ == "__main__":
    customer = CustomerProfile(
        anticaptcha_api_key="... your key here ...",  # Anti-captcha API Key (auto_captcha=False to disable it)
        auto_captcha=False,  # Enable anti-captcha plugin (if False, you have to solve reCaptcha manualy and press ENTER in the Terminal)
        auto_office=True,
        chrome_driver_path="/usr/local/bin/chromedriver",
        # chrome_profile_name="Profile 7",  # Profile name
        # chrome_profile_path=f"{os.curdir}/chrome_profiles/",  # You can persist Chrome profile between runs, it's good for captcha :)
        save_artifacts=True,  # Record available offices / take available slots screenshot
        telegram_token="",  # Your Telegram bot token (sms-confirm cita through a bot using command "/code 12345")
        # wait_exact_time = [
        #     [0, 0], # [minute, second]
        #     [15, 0],
        #     [30, 0],
        #     [45, 0],
        # ],
        province=Province.BARCELONA,
        operation_code=OperationType.CERTIFICADOS_UE,
        doc_type=DocType.PASSPORT,  # DocType.NIE or DocType.PASSPORT
        doc_value="XY1234567",  # NIE or Passport number, no spaces.
        country="ITALIA",
        name="PINCO PALLINO",  # Your Name
        phone="612345678",  # Phone number (use this format, please)
        email="pinco.pallino@gmail.com",  # Email
        year_of_birth="1990",
        # Offices in order of preference
        # This selects specified offices one by one or a random one if not found.
        # For recogida only the first specified office will be attempted or none
        offices=[Office.BARCELONA_MALLORCA],
    )
    if "--autofill" not in sys.argv:
        try_cita(context=customer, cycles=9999)  # Try 200 times
    else:
        from mako.template import Template

        tpl = Template(
            filename=os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "bcncita/template/autofill.mako"
            )
        )
        print(tpl.render(ctx=customer))  # Autofill for Chrome


# In Terminal run:
#   python3 example1.py
# or:
#   python3 example1.py --autofill
