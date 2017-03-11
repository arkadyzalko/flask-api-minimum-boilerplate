from flask import Flask
from config import config
import logging
from .api_v1 import api_v1 as api_v1_blueprint

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def create_app(env):
    logger.info('Environment in __init__: "%s"', env)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config[env])

    config[env].init_app(app)

    # Blueprints
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app
