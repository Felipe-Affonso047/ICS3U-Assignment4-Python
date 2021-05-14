#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program resolves the quadratic function


def main():
    # this function resolves the quadratic function
    print("This program solves quadratics equations.\n")
    print("Every quadratic equation can be represented by ax² + bx + c = 0.")

    try:
        a = float(input("Insert a: "))
        b = float(input("Insert b: "))
        c = float(input("Insert c: "))
        descriptant = (b ** 2) - (4 * a * c)

        print()
        if a != 0:
            if descriptant > 0:
                x1 = (descriptant ** (1 / 2) - b) / (2 * a)
                x2 = (- descriptant ** (1 / 2) - b) / (2 * a)

                print("x1 = {}".format(x1))
                print("x2 = {}".format(x2))
            elif descriptant == 0:
                x = (- b) / (2 * a)

                print("x = {}".format(x))
            else:
                print("There is no value for x.")
        else:
            print(
                "This input is invalid, please, "
                "insert an number different from 0 for a.")
    except Exception:
        print("\nThis input is invalid, please, insert an number.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
