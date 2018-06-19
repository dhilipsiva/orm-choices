# ORM Choices
A helpful decorator for choice fields (Django choices or SQLAlchemy ChoiceType). Do choices the pythonic way.

## Why create ORM Choices?

I got sick and tired of using `choice` fields in Django ORM and SQLAlchemy. [Look here for a context](https://github.com/pythonindia/junction/issues/302)

For example:

```python
# Conference Application Choice Fields
CONFERENCE_STATUS_ACCEPTING_CFP = "Accepting Proposals"
CONFERENCE_STATUS_CLOSED_CFP = "Proposal submission closed"
CONFERENCE_STATUS_ACCEPTING_VOTES = "Accepting Votes"
CONFERENCE_STATUS_SCHEDULE_PUBLISHED = "Schedule Published"

CONFERENCE_STATUS_LIST = ((1, CONFERENCE_STATUS_ACCEPTING_CFP),
                          (2, CONFERENCE_STATUS_CLOSED_CFP),
                          (3, CONFERENCE_STATUS_ACCEPTING_VOTES),
                          (4, CONFERENCE_STATUS_SCHEDULE_PUBLISHED),
                          )

# Using it in a model:

class Conference(Model):
    status = models.PositiveSmallIntegerField(
		default=1, choices=CONFERENCE_STATUS_LIST)
```

I have no Idea what 1 is (I mean its not really obvious that it means `CONFERENCE_STATUS_ACCEPTING_CFP` when `CONFERENCE_STATUS_LIST` is declared in some other file).


I needed a clean and DRY way of making use of Choice Fields.

Introducing `choices`:


```python

from orm_choices import choices

@choices
class ConferenceStatus:
	class Meta:
    	ACCEPTING_CFP = [1, "Accepting Proposals"]
    	CLOSED_CFP = [2, "Proposal submission closed"]
    	ACCEPTING_VOTES = [3, "Accepting Votes"]
    	SCHEDULE_PUBLISHED = [4, "Schedule Published"]

# Using it in a model:

class Conference(Model):
    status = models.PositiveSmallIntegerField(
		default=ConferenceStatus.ACCEPTING_CFP,
		choices=ConferenceStatus.CHOICES)
```

What did just happen? Crazy (not really). I know, right! Declare all your variables in `Meta` class (within `ConferenceStatus`). And apply the `orm_choices` decorator to `ConferenceStatus` class. And boom! Your `ConferenceStatus` now has these attributes:

```python
ConferenceStatus.ACCEPTING_CFP  # This will return `1`
ConferenceStatus.ACCEPTING_VOTES  # This will return `2`

# And so on...
```
And it will add a new `CHOICES` attribute too.

```
print(ConferenceStatus.CHOICES)
# Will Print
((1, "Accepting Proposals"), (2, "Proposal submission closed"), (3, "Accepting Votes"), (4, "Schedule Published"))
```

Clean and DRY!

## Utils

### Curreny Codes

```
from orm_choices.utils.currency_code import CurrencyCode

```
