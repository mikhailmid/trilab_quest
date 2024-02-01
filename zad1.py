from typing import Optional


class Processor:

    def process(self, dta: Optional[dict]) -> tuple:
        return tuple(dta.items() or {})


class ExtendedProcessor(Processor):
    def process(self, dta: Optional[dict]) -> tuple:
        data = super().process(dta)
        data += ("extension", True)
        return data

