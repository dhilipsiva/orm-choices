from orm_choices import choices


@choices
class BloodType:
    class Meta:
        A_POSITIVE = [1, 'A +ve']
        B_POSITIVE = [2, 'B +ve']
        O_POSITIVE = [3, 'O +ve']
        AB_POSITIVE = [4, 'AB +ve']
        A_NEGATIVE = [-1, 'A -ve']
        B_NEGATIVE = [-2, 'B -ve']
        O_NEGATIVE = [-3, 'O -ve']
        AB_NEGATIVE = [-4, 'AB -ve']
