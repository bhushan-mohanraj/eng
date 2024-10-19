from dataclasses import dataclass


# TODO: Send `today` to the templates.


@dataclass
class BaseConfig:
    """
    The base configuration for a newspaper.
    """

    name: str

    website_url: str
    website_display_url: str
    view_in_browser_url: str

    header_image_url: str

    join_url: str
    contact_url: str

    tip_url: str
    donate_url: str
    submit_url: str


@dataclass
class BaseSocialConfig:
    """
    The configuration of social links for a newspaper.
    """


# All links and images are from The Daily's website as of 2024-10-18.
# The special links are Mailchimp merge tags.
THE_DAILY_BASE_CONFIG = BaseConfig(
    name="The Stanford Daily",
    website_url="https://stanforddaily.com/",
    website_display_url="stanforddaily.com",
    view_in_browser_url="*|ARCHIVE|*",
    header_image_url="https://stanforddaily.com/wp-content/uploads/2019/11/cropped-DailyLogo-CardinalRed.png",
    join_url="https://stanforddaily.com/join/",
    contact_url="https://stanforddaily.com/contact-us/",
    tip_url="https://stanforddaily.com/tips/",
    donate_url="https://stanforddaily.com/donate/",
    submit_url="https://stanforddaily.com/submitting-to-the-daily/",
)
