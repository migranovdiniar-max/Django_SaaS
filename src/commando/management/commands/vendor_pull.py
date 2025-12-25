from django.core.management.base import BaseCommand
import helpers
from django.conf import settings


STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")


VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map",
}


class Command(BaseCommand):
    help = "Prints 'Hello, World!' to the console."

    def handle(self, *args, **options):
        self.stdout.write("Downloading vendor static files")

        completed_urls = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                completed_urls += [url]
            else:
                self.stdout.write(f"Failed to download {url}")

        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(f"Successfully downloaded all vendor static files")
        else:
            self.stdout.write(f"Failed to download all vendor static files")
