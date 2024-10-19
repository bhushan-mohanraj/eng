from dataclasses import dataclass


# TODO: Send `today` to the templates.


@dataclass
class BaseConfig:
    """
    The base configuration for a newspaper.
    """

    website_url: str
    website_display_url: str
    view_in_browser_url: str

    header_image_url: str

    tip_url: str
    donate_url: str
    submit_url: str


@dataclass
class BaseSocialConfig:
    """
    The configuration of social links for a newspaper.
    """


# Links and images as of 2024-10-18.
# The special links are Mailchimp merge tags.
THE_DAILY_BASE_CONFIG = BaseConfig(
    website_url="https://stanforddaily.com/",
    website_display_url="stanforddaily.com",
    view_in_browser_url="*|ARCHIVE|*",
    header_image_url="https://stanforddaily.com/wp-content/uploads/2019/11/cropped-DailyLogo-CardinalRed.png",
    tip_url="https://stanforddaily.com/tips/",
    donate_url="https://stanforddaily.com/donate/",
    submit_url="https://stanforddaily.com/submitting-to-the-daily/",
)
