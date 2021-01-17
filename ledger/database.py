from ledger.config import DatabaseConfig


def build_db_uri() -> str:
    """Use information from the config file to build a PostgreSQL URI."""
    if DatabaseConfig.uri:
        return DatabaseConfig.uri

    return (
        f"postgresql://{DatabaseConfig.username}:{DatabaseConfig.password}"
        f"@{DatabaseConfig.host}:{DatabaseConfig.port}/{DatabaseConfig.database}"
    )
