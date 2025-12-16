import importlib.util

def load_mail_module(path):
    """Load a Python module from the given file path using importlib (3.12+ safe)."""
    spec = importlib.util.spec_from_file_location('mail_module', path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader, "Invalid module spec"
    spec.loader.exec_module(module)
    return module

def send_mail(address, message):
    print(f"Sending mail to {address}")
    print(message)
