"""Costing Playground Shell"""

# Built-ins
import os
import IPython
from traitlets.config import Config

# Shared
from src.modules.shared.infrastructure import Bootstrap

# Registries
# Import here your registries

bootstrap = Bootstrap(
    registries=[
        # Inject to the bootstrap your registries
    ],
    debug=False
)

c = Config()

message = """
   _____ __         ____   ____  __                                             __
  / ___// /_  ___  / / /  / __ \/ /___ ___  ______ __________  __  ______  ____/ /
  \__ \/ __ \/ _ \/ / /  / /_/ / / __ `/ / / / __ `/ ___/ __ \/ / / / __ \/ __  / 
 ___/ / / / /  __/ / /  / ____/ / /_/ / /_/ / /_/ / /  / /_/ / /_/ / / / / /_/ /  
/____/_/ /_/\___/_/_/  /_/   /_/\__,_/\__, /\__, /_/   \____/\__,_/_/ /_/\__,_/   
                                     /____//____/                                 

                                Build by Royer Guerrero
"""
c.InteractiveShellApp.exec_lines = [
    'print("""{}""")'.format(message),
]

IPython.start_ipython(argv=[], user_ns={
    'bootstrap': bootstrap,
}, config=c)

