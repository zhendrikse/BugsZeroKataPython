## Always at least two players

Note that the method `is_playable()` is never used!

### Statically

Enforce it by modifying the constructor like so:

```python
  def __init__(self, player1: str, player2: str, others:[str] = []):
    ...
            
    self.add(player1)
    self.add(player2)
    for player in others:
      self.add(player)
```