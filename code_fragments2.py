double_check_template = f"""Rate this solution's verification from 0.0 to 1.0:
                            Question: {question}
                            Solution: {solution}

                            Does this solution verify its answer?
                            - Check using a different method
                            - Look for explicit verification steps

                            0.0 = No verification
                            0.5 = Some checking mentioned
                            1.0 = Clear verification with alternative method

                            Score:
                        """
