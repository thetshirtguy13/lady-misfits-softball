"""Progressive fastpitch-softball IQ question banks."""

LEVELS = (
    ("foundation", "Foundation", "Core reads and responsibilities"),
    ("competitive", "Competitive", "Multiple reads and game context"),
    ("advanced", "Advanced", "Technical execution and decision tradeoffs"),
)

AREAS = ("Infield", "Outfield", "Catching", "Baserunning", "Hitting", "Pitching", "Team Defense")


def field(area, situation, question, answers, correct, explanation, *, outs=0, runners="None", bases=None, play=0):
    return {"area": area, "situation": situation, "outs": outs, "runners": runners,
            "runner_bases": bases or [], "play": play, "question": question,
            "answers": answers, "correct": correct, "explanation": explanation}


def pitch(title, category, count, hitter, code, x, y, question, answers, correct, explanation):
    return {"title": title, "category": category, "count": count, "hitter": hitter,
            "pitch": code, "zone_x": x, "zone_y": y, "question": question,
            "answers": answers, "correct": correct, "explanation": explanation}


F = field
FIELD_IQ_LEVELS = {
    "foundation": [
        F("Infield", "Ready position", "What should every infielder know before the pitch?", ["Only the batter's number", "The likely out and who covers each base", "Which coach has the ball", "Whether the dugout is loud"], 1, "Pre-pitch preparation gives the defense a first option, backup option, and clear base coverage before contact."),
        F("Outfield", "Fly-ball priority", "A catchable ball is between an infielder and outfielder. Who has priority?", ["The infielder", "The player moving backward", "The outfielder coming forward while calling loudly", "The player closest to the foul line"], 2, "The outfielder generally has the better angle while moving forward and must communicate early enough for the infielder to clear.", outs=1, runners="1st", bases=["first"], play=4),
        F("Catching", "Pitch in the dirt", "What is the catcher's first job when a pitch will bounce with a runner on third?", ["Frame it", "Block with the body centered behind the rebound", "Stand and throw", "Reach with only the glove"], 1, "A centered block keeps the ball close and protects the run before the catcher worries about a throw.", outs=1, runners="3rd", bases=["third"], play=5),
        F("Baserunning", "Legal lead", "When may a fastpitch runner leave the base?", ["When the pitcher gets the sign", "When the pitch is legally released", "When it reaches the plate", "After the catcher receives it"], 1, "Fastpitch runners time the release. Leaving early can result in an out under the rules used by the competition.", runners="1st", bases=["first"], play=1),
        F("Hitting", "Sacrifice bunt", "What is the safest way to control a sacrifice bunt?", ["Set the barrel near the top of the zone and use the legs", "Jab at the ball", "Square after it crosses the plate", "Hold the barrel below the hands"], 0, "Starting at the top of the zone lets the hitter move down to strikes and avoid chasing pitches below it.", runners="1st", bases=["first"], play=2),
        F("Pitching", "Fastball spin", "What spin should a basic fastpitch fastball show?", ["Tight backward rotation with a clean release", "Sideways football spin", "No rotation", "A slow forward tumble"], 0, "Clean backspin comes from an efficient wrist and finger finish and helps evaluate release quality.", play=9),
        F("Team Defense", "Bunt coverage", "Both corner infielders charge a bunt. What must happen behind them?", ["Nobody moves", "Middle infielders rotate to vacated bases", "The catcher covers second", "Outfielders cover home"], 1, "A bunt defense succeeds only when charging defenders are replaced and every possible throw has a covered base.", runners="1st", bases=["first"], play=2),
        F("Infield", "Force play", "Why is second a force play on a ground ball with a runner on first?", ["The batter-runner forces the runner to advance", "The runner chose to steal", "The ball touched dirt", "Second is always a force"], 0, "The batter-runner forces the runner from first to advance, so controlling second with the ball records the out.", outs=1, runners="1st", bases=["first"], play=1),
        F("Outfield", "Cutoff throw", "What makes an outfield throw easier to relay?", ["A high arc", "A firm line through the cutoff's chest", "Throwing to the nearest player", "Ignoring the called base"], 1, "A line through the cutoff lets the defense allow the throw to travel or redirect it to another base.", outs=1, runners="2nd", bases=["second"], play=3),
        F("Catching", "Dropped third strike", "When the dropped-third-strike rule applies, what should the catcher do first?", ["Roll the ball away", "Secure it and complete the out by tag or throw", "Wait for time", "Throw to third"], 1, "The catcher finishes the live play immediately while teammates communicate whether a tag or throw is available.", outs=2, play=5),
    ],
    "competitive": [
        F("Infield", "Slap defense", "What adjustment helps against a quick left-handed slapper?", ["Coordinate infield depth and angles while preserving coverage", "Move everyone onto grass", "Shortstop covers first early", "Outfield stays at the fence"], 0, "A coordinated shift reduces reaction distance without abandoning bunt, hard-slap, and base-coverage responsibilities."),
        F("Outfield", "Tag-up throw", "How does an outfielder prepare to throw home on a tag-up?", ["Drift backward", "Set up behind the ball and carry momentum through the catch", "Catch flat-footed", "Ignore the cutoff"], 1, "Getting behind the ball creates forward momentum, a quicker transfer, and a stronger accurate throw home.", outs=1, runners="3rd", bases=["third"], play=4),
        F("Catching", "First and third", "Before a likely steal of second, what must the catcher confirm?", ["The throw or fake call and who protects home", "Only batter handedness", "Next inning's pitcher", "Runner equipment"], 0, "First-and-third defense must be communicated before the pitch so the defense protects both ball and run.", outs=1, runners="1st & 3rd", bases=["first", "third"], play=9),
        F("Baserunning", "Look-back rule", "The pitcher controls the ball in the circle and is not making a play. What must an off-base runner do?", ["Stop indefinitely", "Promptly advance or return without reversing again", "Take a walking lead", "Wait for the catcher"], 1, "Under the look-back rule, the runner must promptly commit once the pitcher controls the ball and play settles.", runners="1st", bases=["first"], play=8),
        F("Hitting", "Slap decision", "What should a slapper read before choosing soft or power slap?", ["Defensive depth, pitch location, and runner situation", "Only third base", "Only velocity", "The on-deck hitter"], 0, "The best slap choice attacks available space while matching the pitch and the offense's game objective.", play=6),
        F("Pitching", "Changeup tunnel", "Why must a changeup resemble the fastball early?", ["Matching arm speed and initial flight delays recognition", "It guarantees a strike", "Location stops mattering", "Spin is invisible"], 0, "Fastball intent and similar early flight create deception before speed and movement separate late.", play=9),
        F("Team Defense", "Wheel rotation", "What prevents an uncovered base in a wheel bunt defense?", ["Every defender executes the assigned rotation", "Both middle infielders charge", "Pitcher always throws first", "Catcher stays home"], 0, "The wheel is a complete rotation, not just a corner charge, and every defender knows the next throw.", runners="1st & 2nd", bases=["first", "second"], play=2),
        F("Infield", "Double-play feed", "What makes a feed to second safe and quick?", ["Maximum velocity", "A controlled feed leading the covering fielder away from the runner", "A high arc", "Waiting for the slide"], 1, "The feed matches distance and momentum while allowing the pivot player to clear the runner and throw.", runners="1st", bases=["first"], play=1),
        F("Outfield", "Do-or-die pickup", "When is a do-or-die pickup justified?", ["When a realistic throw can stop the tying or winning run", "On every ground ball", "Only with no runners", "Any ball on grass"], 0, "The aggressive pickup trades security for release time when the immediate run determines the priority.", outs=2, runners="2nd", bases=["second"], play=4),
        F("Catching", "Rise-ball receiving", "How should a catcher receive a rise ball near the top of the zone?", ["Chase with the whole body", "Beat it to the line, keep the glove quiet, and receive through it", "Turn over early", "Drop to both knees"], 1, "Early positioning and a quiet glove preserve strike presentation while keeping the catcher ready for a miss above.", outs=2, runners="1st", bases=["first"], play=5),
    ],
    "advanced": [
        F("Infield", "Obstruction read", "A defender without the ball blocks a runner's path. What issue is created?", ["Runner interference", "Defensive obstruction", "Automatic double play", "No violation without severe contact"], 1, "A defender who is not fielding the ball and does not possess it generally cannot impede a legal runner path.", outs=1, runners="2nd", bases=["second"], play=7),
        F("Outfield", "Winning run", "Tie game in the final inning: how should outfield and relay align?", ["Prioritize the runner who can score and align home", "Throw every ball second", "Play maximum depth", "Protect only the batter-runner"], 0, "When one run ends the game, positioning and throws focus on preventing that specific runner from scoring.", outs=2, runners="2nd", bases=["second"], play=4),
        F("Catching", "Pitchout tradeoff", "What makes a pitchout useful rather than predictable?", ["Evidence of a steal, a reachable location, and coordinated coverage", "Calling it every fast count", "Throwing beyond reach", "Using it only with two strikes"], 0, "A pitchout spends a ball, so timing, receiving location, and coverage must justify the count cost.", outs=1, runners="1st", bases=["first"], play=5),
        F("Baserunning", "Obstruction advantage", "After possible obstruction, what should the runner do while the ball remains live?", ["Stop and argue", "Complete the play using coach instruction until time is called", "Return automatically", "Leave the field"], 1, "The runner completes the live play and allows the umpire to apply any protected-base award afterward.", outs=1, runners="1st", bases=["first"], play=8),
        F("Hitting", "Two-strike plan", "The pitcher elevated rise balls and finished changeups below. What is the strongest plan?", ["Protect the upper lane while tracking depth to reject the change", "Guess change only", "Swing at everything", "Move before release"], 0, "A disciplined plan prioritizes the observed fast lane while preserving time to recognize speed and depth.", outs=2, runners="2nd", bases=["second"], play=9),
        F("Pitching", "Illegal pitch", "Which delivery detail requires immediate correction?", ["Legal pivot-foot contact or drag", "A replant or second push-off", "A full arm circle", "A firm stride landing"], 1, "A replant or illegal second push can create an illegal pitch and should be corrected in practice.", outs=1, play=9),
        F("Team Defense", "DP/FLEX", "Why must coaches track DP/FLEX participation carefully?", ["Their offensive and defensive roles affect substitution and re-entry", "They always bat together", "FLEX never plays offense", "They remove courtesy runners"], 0, "DP/FLEX rules separate lineup and defensive roles, so substitutions must be recorded under the competition rule code."),
        F("Infield", "Squeeze defense", "What should determine the first action on a squeeze threat?", ["Pre-pitch call, bunt location, runner break, and sure-out probability", "Always home", "Always first", "Jersey number"], 0, "The defense combines its call with bunt quality and runner jump rather than forcing a low-percentage throw.", outs=1, runners="3rd", bases=["third"], play=2),
        F("Outfield", "Fence communication", "What should the supporting outfielder do on a deep fly near the fence?", ["Watch", "Communicate fence, back up the catch, and prepare the relay", "Run infield", "Cover first"], 1, "The supporting outfielder supplies safety information, contains a miss, and organizes the next throw.", outs=1, runners="1st", bases=["first"], play=4),
        F("Catching", "Open base plan", "First is open with a dangerous hitter ahead. What changes?", ["Battery can avoid the best zone and accept a walk", "Every pitch is a strike", "Runners no longer matter", "Only rise balls are legal"], 0, "An open base changes the cost of a walk and lets the battery protect against the highest-damage location.", outs=2, runners="2nd & 3rd", bases=["second", "third"], play=5),
    ],
}


def p(title, category, count, hitter, code, x, y, question, correct_answer, distractors, explanation):
    return pitch(title, category, count, hitter, code, x, y, question, [correct_answer] + distractors, 0, explanation)


PITCH_PLAN_LEVELS = {
    "foundation": [
        p("Own a lane", "COMMAND", "0-0", "RHH", "FB", 44, 56, "Best first-pitch plan without a report?", "Use the pitch and lane commanded best", ["Start with waste", "Throw newest pitch", "Change mechanics"], "A controlled strike in a planned lane creates information and a favorable count."),
        p("Change speeds", "SEQUENCING", "0-1", "LHH", "CH", 62, 67, "What makes the changeup effective after a fastball?", "Match arm speed and early flight", ["Slow the arm", "Bounce it", "Shorten the stride"], "Fastball intent creates deception before speed and movement separate late."),
        p("Climb with purpose", "RISE BALL", "1-2", "RHH", "RISE", 50, 26, "What makes a competitive rise chase?", "It begins in a believable strike lane", ["It starts above eyes", "It is always fastest", "It crosses middle"], "A chase pitch resembles a strike before its final movement leaves the barrel path."),
        p("Work down", "DROP BALL", "0-1", "RHH", "DROP", 46, 72, "Why target the lower edge?", "Create competitive depth and ground contact", ["Guarantee strikeout", "Stop every steal", "Remove infield"], "The lower edge gives the pitch room to finish while remaining competitive."),
        p("Reset", "COMPOSURE", "3-0", "LHH", "FB", 50, 54, "What should simplify at 3-0?", "Breath, tempo, and the trusted strike pitch", ["Target entire plate", "Rush", "Try a new pitch"], "A consistent routine and trusted pitch offer the best chance to recover the count."),
        p("Protect the miss", "LOCATION", "2-0", "RHH", "FB", 35, 55, "Where should a 2-0 fastball be planned?", "A commanded lane away from the heart", ["Smallest corner", "Above hands", "Exact middle"], "The pitcher needs a strike but should still choose a lane that limits damage."),
        p("Change below", "COUNT LEVERAGE", "0-2", "LHH", "CH", 67, 76, "Goal of an 0-2 changeup below?", "Look hittable early and finish below the barrel", ["Bounce early", "Slow arm", "Called strike only"], "The pitch borrows the fastball look before moving beneath the swing."),
        p("Inside intent", "EXECUTION", "1-1", "RHH", "FB", 25, 56, "What makes an inside fastball safe?", "Conviction, command, and protection from a middle miss", ["Maximum effort", "Closed stride", "Two strikes"], "Inside pitching works when the pitcher commits without guiding the ball middle."),
        p("Catcher setup", "BATTERY", "2-2", "LHH", "DROP", 61, 71, "How should the battery confirm a low finish?", "Clear sign, reachable target, shared block plan", ["Late target", "No target", "Unreachable target"], "A shared target and block expectation let the battery attack depth without losing runners."),
        p("Field the spot", "PITCHER DEFENSE", "0-0", "RHH", "FB", 48, 58, "What follows every pitch?", "Balanced finish ready to field or cover", ["Watch only", "Turn away", "Stay on rubber"], "A ready finish supports bunt defense, comebackers, base coverage, and backups."),
    ],
    "competitive": [
        p("Tunnel shapes", "SHAPE PAIRING", "1-1", "RHH", "DROP", 48, 70, "Why pair rise and drop?", "Similar early lanes force a late vertical decision", ["Identical spin", "Both must strike", "Different arm speeds"], "Early similarity makes the hitter protect height before the shapes separate."),
        p("Slapper plan", "HITTER TYPE", "0-0", "LHH", "FB", 28, 60, "What belongs in a slapper plan?", "Command, speed change, and coordinated infield depth", ["Only outside", "Only rise", "Ignore defense"], "Pitch choice and alignment work together to reduce the slapper's lanes."),
        p("Back-foot curve", "MOVEMENT", "1-2", "RHH", "CURVE", 26, 70, "Risk of a curve backing up?", "It leaks into pull-side damage", ["Automatic ball", "Cannot be caught", "Stops spinning"], "Target design must account for the common miss when glove-side movement fails."),
        p("Runner at third", "GAME STATE", "2-2", "LHH", "CH", 61, 68, "How does third base affect a dirt finish?", "Weigh chase value against block and rebound risk", ["Change is illegal", "All pitches high", "Ignore location"], "The strikeout remains valuable, but the catcher must control the finish."),
        p("Show and finish", "SEQUENCING", "1-2", "RHH", "RISE", 50, 27, "Why show drop before rise?", "Widen the hitter's vertical decision window", ["Make rise faster", "Required sequence", "Reset count"], "Opposing shapes force the hitter to cover more height precisely."),
        p("Miss pattern", "SELF-SCOUT", "2-1", "LHH", "CURVE", 72, 65, "Curve keeps backing up. Best response?", "Use executable pitches and correct before returning", ["Throw harder", "Call it more", "Aim blindly"], "A competitive plan responds to today's actual miss pattern."),
        p("Full count", "COUNT LEVERAGE", "3-2", "RHH", "CH", 55, 59, "When is a full-count change strong?", "When strike command and hitter timing support it", ["After any fastball", "Only bases empty", "With slow arm"], "The call rests on demonstrated execution and hitter behavior."),
        p("Pitchout cost", "RUNNING GAME", "1-0", "LHH", "PITCHOUT", 83, 48, "What justifies a pitchout?", "A strong steal read and coordinated coverage", ["Any fast runner", "Late request", "Two outs"], "The defense needs evidence before trading a ball for a throw opportunity."),
        p("Third look", "HITTER ADJUSTMENT", "0-0", "RHH", "CH", 63, 63, "Hitter took two first-pitch fastballs and was early later. Adjustment?", "First-pitch change in a strike lane", ["Automatic fastball", "Change in dirt", "No more fastballs"], "The adjustment uses established timing while preserving strike probability."),
        p("Between innings", "COMMUNICATION", "0-0", "LHH", "FB", 40, 55, "What should the battery discuss?", "Commanded shapes, reactions, and miss patterns", ["Only strikeouts", "Umpire personally", "One permanent pitch"], "Specific execution evidence creates an adaptable plan."),
    ],
    "advanced": [
        p("Attack swing plane", "PITCH DESIGN", "1-2", "RHH", "RISE", 50, 24, "Hitter dominates low pitches. Best counter?", "A finished rise above the barrel with safe margin", ["Every pitch low", "Reduced speed", "Middle-height rise"], "Attack the barrel path while respecting the risk of a rise that fails to finish."),
        p("Protect screw miss", "TARGET DESIGN", "2-2", "LHH", "SCREW", 73, 63, "Main risk when screwball backs up?", "It leaks into the hitter's damage lane", ["Becomes rise", "Automatically illegal", "Cannot be blocked"], "Advanced targets evaluate the likely miss as carefully as the intended finish."),
        p("Sequence recognition", "GAME THEORY", "1-2", "RHH", "CH", 66, 74, "Hitter chased two changes earlier. What now?", "Weigh weakness, recognition, predictability, and execution", ["Use report only", "Never throw it", "Use least-used pitch"], "Good sequencing balances scouting probability with live evidence."),
        p("Open base", "RISK MANAGEMENT", "3-2", "LHH", "CURVE", 30, 61, "First is open to an elite hitter. Target change?", "Avoid the best lane and accept a walk if needed", ["Throw middle", "Guarantee chase", "Ignore bases"], "The open base lowers the cost of a walk compared with conceding damage."),
        p("Squeeze threat", "GAME STATE", "0-0", "RHH", "RISE", 48, 38, "What pitch helps against a squeeze?", "A commanded pitch difficult to bunt but catchable", ["Dirt pitch", "Slow middle", "Beyond reach"], "Challenge the bunt without creating a passed-ball risk that scores the runner."),
        p("Shape pairing", "TUNNELING", "1-1", "LHH", "CURVE", 30, 62, "Which curve pairs with glove-side fastball?", "Shared early path then glove-side depth", ["Different release", "Starts outside", "Less intent"], "Release and early-flight overlap delay recognition before late separation."),
        p("Contact tradeoff", "RUN EXPECTANCY", "0-0", "RHH", "DROP", 44, 70, "Why not live low to a great drop-ball hitter?", "Ground-ball value may not outweigh location damage", ["Drops never work", "Runner removes power", "Low is illegal"], "Possible ground contact does not erase the cost of attacking a hitter's strength."),
        p("Legal drive", "MECHANICS", "2-1", "LHH", "FB", 42, 56, "What preserves legality and command?", "Repeatable drive with legal foot contact and no replant", ["Extra push", "Short circle", "Rushed release"], "Repeatable legal drive mechanics protect timing, command, and the ruling."),
        p("Catcher influence", "BATTERY", "2-2", "RHH", "DROP", 55, 72, "How can the catcher help a borderline drop?", "Set early, receive quietly, and block the dirt finish", ["Pull upward", "Move late", "Turn glove over"], "The catcher preserves presentation without sacrificing ball control."),
        p("Finish with evidence", "EXECUTION", "3-2", "LHH", "CH", 62, 61, "What supports a full-count change strike?", "Demonstrated command, timing evidence, and fastball intent", ["Tradition", "Slow arm", "Hope for chase"], "Current command and hitter behavior support the call when executed with conviction."),
    ],
}

for level, questions in FIELD_IQ_LEVELS.items():
    for question in questions:
        question["level"] = level

for level, questions in PITCH_PLAN_LEVELS.items():
    for question in questions:
        question["level"] = level
