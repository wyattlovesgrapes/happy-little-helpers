from happy_little_helpers.flash_env import get_flash_path, read_env
from happy_little_helpers.debugger import enable_debug_mode

enable_debug_mode()

flash_path = get_flash_path('code-tests')

read_env(flash_path)

