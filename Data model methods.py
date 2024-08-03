{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "5dd9725a-e2f4-4b08-b5e1-b072aab3804a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Polynomial((4, 6, 8))\n",
      "Length of polynomial p1: 3\n"
     ]
    }
   ],
   "source": [
    "class Polynomial:\n",
    "    def __init__(self, *coeffs):\n",
    "        self.coeffs = coeffs\n",
    "\n",
    "    def __repr__(self):\n",
    "        return 'Polynomial({!r})'.format(self.coeffs)\n",
    "\n",
    "    def __add__(self, other):\n",
    "        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))\n",
    "\n",
    "    def __len__(self):\n",
    "        return len(self.coeffs)\n",
    "\n",
    "    def __call__(self, x):\n",
    "          return polynomial(*(x+Y for x,y in zip(self.coeffs, othercoeffs)))\n",
    "\n",
    "\n",
    "p1 = Polynomial(1, 2, 3)\n",
    "p2 = Polynomial(3, 4, 5)\n",
    "p3=p1+p2\n",
    "print(p3)\n",
    "print(\"Length of polynomial p1:\", len(p1))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5240bafb-b5a1-45ad-a0c4-b1b92f135876",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "704e5e39-b441-4cef-90d0-57c93f122dc6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
