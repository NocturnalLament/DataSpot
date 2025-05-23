from dataclasses import dataclass
from typing import Optional, Dict, List


@dataclass()
class PlaylistSearchObject:
    external_urls: Dict[str, str]
    href: str
    limit: int
    next: Optional[str]
    offset: int
    previous: Optional[str]
    total: int

@dataclass()
class PlaylistImages:
    url: str
    width: Optional[int]
    height: Optional[int]

@dataclass()
class PlaylistSearchOwner:
    external_urls: Dict[str, str]
    href: str
    id: str
    type: str
    uri: str
    display_name: Optional[str] = None

@dataclass()
class PlaylistObject:
    collaborative: int
    description: str
    external_urls: dict
    href: str
    id: str
    images: List[PlaylistImages]
    name: str
    owner: PlaylistSearchOwner
    primary_color: str
    public: bool

@dataclass()
class AlbumSearchResult:
    href: str
    limit: int
    next: Optional[str]
    offset: int
    previous: Optional[str]
    total: int
    items: List[PlaylistObject]
