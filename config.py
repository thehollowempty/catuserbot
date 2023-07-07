from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 17429069
    API_HASH = "dc1a8101cd63983a45ab832ff2bf5673"
    # the name to display in your alive message
    ALIVE_NAME = "𝒯𝑒𝒹𝒹𝓎"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://gffenxjz:9F1Vhb7ZBqfmZ-R0_hFRZkq1ltbn3XQL@trumpet.db.elephantsql.com/gffenxjz"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOGsBu6GQ5r79RNPLl21UN0ihli2oZojs1-4fz7ixQ4fYBbmr_Et1MkTOcvAJGozBQzjZsGHlGkkJ1JC3Oa7PvD6Iq8ktZZKmyaLyxHowrleejXgGHCalgRW2v3elmbOumnEBg55qAHvEeGgU9MwVp-4_MpNI3pxnwuGzYmK6gkYkffOODFv834VPiLqok6cS14CErV7qNBIfz7C3l4Lhjj5j41IHlALMlDI9dKMhjcoqesQ3s0f32Z7I2P1GyGdpIiR6-enywJhOy-dkLuBuYhxjh6ZJM7iJ3wMeJLEk09qZwCE4x_h1tIG4G8Ci344YHG0wu0b2I4U6aUgm9MQS8qcr3dw="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6049789485:AAEjexSzMynfLZ90SxtOFqkxvm9-p9f-yvU"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001521186818
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
