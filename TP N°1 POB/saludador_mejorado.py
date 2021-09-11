#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Este es un saludador personalizado: ¡Toma tu nombre y apellido y te responde!')
parser.add_argument('-n', '--name',
                    type=str,
                    help='set your name')
parser.add_argument('-l', '--lastname',
                    type=str,
                    help='set your lastname',
                    default='')

args = parser.parse_args()

print(f"¡Hola {args.name} {args.lastname}! ¡Bienvendix!")
