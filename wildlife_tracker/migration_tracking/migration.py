from typing import Any

from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:

    def __init__(self,
                migration_id: int,
                current_date: str,
                current_location: str,
                migration_path: MigrationPath,
                start_date: str,
                status: str = "Scheduled") -> None:
        self.migration_id = migration_id
        self.current_date = current_date
        self.current_location = current_location
        self.migration_path = migration_path
        self.start_date = start_date
        self.status = status

    def update_migration_details(self, **kwargs: Any) -> None:
        pass

    def get_migration_details(self) -> dict[str, Any]:
        pass

    def cancel_migration(self) -> None:
        pass
