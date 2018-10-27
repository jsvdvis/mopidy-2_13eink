import pykka
import logging
from mopidy import core

logger = logging.getLogger("mopidy-2_13eink")

class EinkFrontend(pykka.ThreadingActor, core.CoreListener):
    def __init__(self, config, core):
        super(EinkFrontend, self).__init__()
        self.core = core
    
    def on_event(self, event, **kwargs):
        logger.debug("Event ocurred" + event)
        print(event)