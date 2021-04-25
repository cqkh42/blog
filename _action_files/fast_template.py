from datetime import datetime
import os
from pathlib import Path
import re
from typing import Optional, Set, Tuple

# Check for YYYY-MM-DD
_re_blog_date = re.compile(r'([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])-)')
# Check for leading dashses or numbers
_re_numdash = re.compile(r'(^[-\d]+)')

warning_type = Tuple[str, str]

def rename_for_jekyll(nb_path: Path, warnings: Optional[Set[warning_type]]=None) -> str:
    """
    Return a Path's filename string appended with its modified time in YYYY-MM-DD format.
    """
    # Checks if filename is compliant with Jekyll blog posts
    return nb_path.with_suffix('.md').name.replace(' ', '-')
