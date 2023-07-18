# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import csv
import googleapiclient.discovery


def comment_processing(response_items):
    comment_list = []

    for res in response_items:
        #handles comment with out replies
        if res["snippet"]["totalReplyCount"] == 0:
            comment = {"id":res["snippet"]["topLevelComment"]["id"], "comment":res["snippet"]["topLevelComment"]["snippet"]["textOriginal"]}
            comment_list.append(comment)
        #handeles comment with replies
        else:
            for resrep in res["replies"]["comments"]:
                comment = {"id":resrep["id"],"comment":resrep["snippet"]["textOriginal"]}
                comment_list.append(comment)

    #for comm in comment_list:
    #    print(comm,"\n************************\n")
    return comment_list

def make_csv(comment_list):
    with open('comments.csv', 'w',encoding='utf8', newline='') as csvfile:
        fieldnames = comment_list[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in comment_list:
            print(row)
            writer.writerow(row)


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    comment_list = []
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyAFLo4JxbimbJ8VRXZn-PynUUzLOQuisxA"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet,replies",
        maxResults=214,
        videoId="0e3GPea1Tyg"
    )
    response = request.execute()
    print(len(response))
    #comment_processing(response["items"])
    make_csv(comment_processing(response["items"]))

if __name__ == "__main__":
    main()