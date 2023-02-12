#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def moto(company, **motorcycles):
    print(f"Company: {company}")
    for bike, max_speed in motorcycles.items():
        print(f"{bike}: {max_speed}")


if __name__ == "__main__":
    moto(
        "ABM",
        Raptor="110 km/h",
        RX_200="95 km/h",
        Road_Star_250="105 km/h",
        GX_250R="140 km/h"
    )
