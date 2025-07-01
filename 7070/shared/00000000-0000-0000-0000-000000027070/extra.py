class Properties:
    thumbnail_fields: set = {"image_url"}
    rewrite_fields: set = {}

    @staticmethod
    def calculate_alpha(_input: dict) -> float:
        alpha = 1.0

        duration = _input.get("duration", 5)
        resolution = _input.get("resolution", "480p")

        if duration == 5:
            if resolution == "480p":
                alpha = 45 / 45
            elif resolution == "720p":
                alpha = 45 / 45
            elif resolution == "1080p":
                alpha = 225 / 45

        elif duration == 10:
            if resolution == "480p":
                alpha = 90 / 45
            elif resolution == "720p":
                alpha = 45 / 45
            elif resolution == "1080p":
                alpha = 450 / 45

        return round(alpha, 2)
