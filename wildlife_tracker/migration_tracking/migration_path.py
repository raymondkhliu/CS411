from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat

class MigrationPath:

    def __init__(self,
                destination: Habitat,
                path_id: int,
                start_location: Habitat,
                species: str,
                duration: Optional[int] = None) -> None:
        self.destination = destination
        self.duration = duration
        self.path_id = path_id
        self.start_location = start_location
        self.species = species

    def get_migration_paths(self) -> list[MigrationPath]:
        pass

    def get_migration_path_details(self) -> dict:
        pass

    def update_migration_path_details(self, **kwargs) -> None:
        pass