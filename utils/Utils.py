class Utils:
    @staticmethod
    def months_to_extended(months):
        years, months = divmod(months, 12)
        extended = f"{years} year{'s' if years > 1 else ''}"

        if months > 0:
            extended += f" and {months} month{'s' if months > 1 else ''}"

        return extended

    @staticmethod
    def to_years(months):
        return months/12
